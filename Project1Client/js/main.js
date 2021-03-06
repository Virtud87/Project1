const url = "http://127.0.0.1:5000/";

/* Validate manager login credentials and send user to manager home page if validation is successful*/
async function managerLogin() {
    const username = document.getElementById("manager-username").value;
    const password = document.getElementById("manager-password").value;
    const credentials = {"username": username, "password": password};

    let response = await fetch(url + "manager/login", {method: "POST", mode: "cors", headers: {
        "Content-Type": "application/json"
        }, body: JSON.stringify(credentials)});
    

    let body = await response.json()
    console.log(body.manager_id);
    if (response.status === 400) {
        alert("Either your username or password or both are incorrect!");
    }
    else if (response.status === 200) {
        sessionStorage.setItem("manager_id", body["manager_id"]);
        window.location.href = "manager_home.html";
    }
    else {
        alert("Something went wrong!");
    }
}


/** Logout */
function managerLogout(managerId) {
    sessionStorage.clear(managerId);
    window.location.href="index.html";
}

/* Return pending requests and dynamically display them when button is clicked */
const tableBody = document.getElementById("table-body-pending");

async function returnPendingRequests() {
    let response = await fetch(url + "pending");
    let requests = await response.json();
    
    if (response.ok) {
        populateData(requests);
    } else {alert("There was a problem returning pending requests.");}
}

function populateData(requestsBody) {
    if (tableBody.innerHTML) {
        tableBody.innerHTML = "";
    } else {
        let count = 1;
        for (let request of requestsBody) {
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td id="request${count}">${request.reimbursementId}</td><td>${request.employeeId}</td><td>${request.date}</td><td>${request.amount}</td><td>${request.reason}</td><td>${request.status}</td><td>${request.comment}</td><td><button onclick="approveRequest(${request.reimbursementId})" class="btn btn-approval">approve</button></td><td><button onclick="denyRequest(${request.reimbursementId})" class="btn btn-approval btn-denial">deny</button></td><td><input id="comment"></input></td>`;
        tableBody.appendChild(tableRow);
        count++;
    }
    }
    
}

/** Submitting approval */
async function approveRequest(reimbursementId) {
    let response = await fetch(url + `approve/${reimbursementId}`, {method: "PATCH", headers: {"Content-Type": "application/json"}});
    tableBody.innerHTML = "";
    returnPendingRequests();
    return response;
}

/** Submitting denial w/ comment */
async function denyRequest(reimbursementId) {
    let comment = document.getElementById("comment").value;
    let response = await fetch(url + `deny/${reimbursementId}`, {method: "PATCH", headers: {"Content-Type": "application/json"}, body: JSON.stringify({comment})});
    tableBody.innerHTML = "";
    returnPendingRequests();
    return response;
}

/** Return Past Reimbursements */
const tablePastBody = document.getElementById("table-body-past");

async function returnPastReimbursements() {
    let response = await fetch(url + "past");
    let pastReimbursements = await response.json();

    if (response.ok) {
    populatePastReimbursements(pastReimbursements);
    } else {alert("There was a problem returning past reimbursements.");}
}

function populatePastReimbursements(pastReimbursementsBody) {
    if (tablePastBody.innerHTML) {
        tablePastBody.innerHTML = "";
    } else {
        for (let reimbursement of pastReimbursementsBody) {
            let tablePastRow = document.createElement("tr");
            tablePastRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.date}</td><td>${reimbursement.amount}</td><td>${reimbursement.reason}</td><td>${reimbursement.status}</td><td>${reimbursement.comment}</td>`;
            tablePastBody.appendChild(tablePastRow);
        }
    }
}

/** -------------------------------------STATISTICS------------------------------------------------- */

/* Total Amount Approved per Employee */
const stat1Body = document.getElementById("stat1-body");

async function returnAmountApproved() {
    let response = await fetch(url + "amount");
    let amountApproved = await response.json();

    if (response.ok) {
        populateAmountApproved(amountApproved);
    } else {alert("There was a problem returning amount approved.");}
}

function populateAmountApproved(amountApprovedBody) {
    if (stat1Body.innerHTML) {
        stat1Body.innerHTML = "";
    } else {
        for (let approval of amountApprovedBody) {
            let tr = document.createElement("tr");
            tr.id = "stats-td";
            tr.innerHTML = `<td>${approval.employeeId}</td><td>${approval.name}</td><td>${approval.totalAmount}</td>`;
            stat1Body.appendChild(tr);
        }
    }
        
}


/* Total Requests Approved per Employee */
const stat2body = document.getElementById("stat2-body");

async function returnRequestsApproved() {
    let response = await fetch(url + "approved/number");
    let requestsApproved = await response.json();

    if (response.ok) {
        populateRequestsApproved(requestsApproved);
    } else {alert("There was a problem returning requests approved.");}
}

function populateRequestsApproved(requestsApprovedBody) {
    if (stat2body.innerHTML) {
        stat2body.innerHTML = "";
    } else {
        for (let request of requestsApprovedBody) {
            let tr = document.createElement("tr");
            tr.innerHTML = `<td>${request.employeeId}</td><td>${request.name}</td><td>${request.totalRequestsApproved}</td>`;
            stat2body.appendChild(tr);
        }
    }
}

/* Total Requests Denied per Employee */
const stat3Body = document.getElementById("stat3-body");

async function returnRequestsDenied() {
    let response = await fetch(url + "denied/number");
    let requestsDenied = await response.json();

    if (response.ok) {
        poplulateRequestsDenied(requestsDenied);
    } else {alert("There was a problem returning requests qpproved.");}
}

function poplulateRequestsDenied(requestsDeniedBody) {
    if (stat3Body.innerHTML) {
        stat3Body.innerHTML = "";
    } else {
        for (let request of requestsDeniedBody) {
            let tr = document.createElement("tr");
            tr.innerHTML = `<td>${request.employeeId}</td><td>${request.name}</td><td>${request.totalRequestsDenied}</td>`;
            stat3Body.appendChild(tr);
        }
    }
}

/* Total Food/Drink Requests Approved per Employee */
const stat4Body = document.getElementById("stat4-body");

async function returnFoodDrinkApproved() {
    let response = await fetch(url + "foodDrink");
    let requestsFoodDrink = await response.json();

    if (response.ok) {
        populateFoodDrinkRequests(requestsFoodDrink);
    } else {alert("There was a problem returning requests.");}
}

function populateFoodDrinkRequests(requestsFoodDrinkBody) {
    if (stat4Body.innerHTML) {
        stat4Body.innerHTML = "";
    } else {
        for (let request of requestsFoodDrinkBody) {
            let tr = document.createElement("tr");
            tr.innerHTML = `<td>${request.employeeId}</td><td>${request.name}</td><td>${request.totalFoodDrinkRequests}</td>`;
            stat4Body.appendChild(tr);
        }
    }
}


/* Total Transportation Requests Approved per Employee */
const stat5Body = document.getElementById("stat5-body");

async function returnTransportationApproved() {
    let response = await fetch(url + "transportation");
    let requestsTransportation = await response.json();

    if (response.ok) {
        populateTransportationRequests(requestsTransportation);
    } else {alert("There was a problem returning requests.");}
}

function populateTransportationRequests(requestsTransportationBody) {
    if (stat5Body.innerHTML) {
        stat5Body.innerHTML = "";
    } else {
        for (let request of requestsTransportationBody) {
            let tr = document.createElement("tr");
            tr.innerHTML = `<td>${request.employeeId}</td><td>${request.name}</td><td>${request.totalTransportationRequests}</td>`;
            stat5Body.appendChild(tr);
        }
    }
}



/** -----------------------------------------------Employee------------------------------------------------ */

/* Validate employee login credentials and send user to employee home page if validation is successful*/
async function employeeLogin() {
    const eusername = document.getElementById("employee-username").value;
    const epassword = document.getElementById("employee-password").value;
    const credentials = {"username": eusername, "password": epassword};

    let response = await fetch(url + "employee/login", {method: "POST", mode: "cors", headers: {
        "Content-Type": "application/json"
        }, body: JSON.stringify(credentials)});

    let body = await response.json()
    if (response.status === 400) {
        alert("Either your username or password or both are incorrect!");
    }
    else if (response.status === 200) {
        sessionStorage.setItem("employee_id", body["employee_id"]);
        window.location.href = "employee_home.html";
    }
    else {
        alert("Something went wrong!");
    }
}


/** Logout */
function employeeLogout(employeeId) {
    sessionStorage.clear(employeeId);
    window.location.href = "index.html";
}

/** Submitting requests */
async function submitRequest() {
    // let reimbursementId = Number(document.getElementById("reimbursementId").value);
    let employeeId = Number(document.getElementById("employeeId").value);
    let date = document.getElementById("date").value;
    let amount = Number(document.getElementById("amount").value);
    let reason = document.getElementById("reason").value;

    let response = await fetch(url + "submission", {method: "POST", 
    headers: {"Content-Type": "application/json", "Accept": "application/json"}, 
    body: JSON.stringify({employeeId, date, amount, reason})});
    let responseBody = await response.json();
    console.log(responseBody);
}

/** View pending requests */
const employeeTableBody = document.getElementById("employee-tableBody");

async function returnEmployeePending() {
    let employeeId = sessionStorage.getItem("employee_id");
    let response = await fetch(url + `reimbursements/${employeeId}`, {method: "GET", 
    headers: {"Content-Type": "application/json", "Accept": "application/json"}});
    let employeeRequests = await response.json();
    console.log(employeeRequests);

    if (response.ok) {
        populateEmployeePending(employeeRequests);
        } else {alert("There was a problem returning past reimbursements.");}
}

function populateEmployeePending(employeeRequestsBody) {
    if (employeeTableBody.innerHTML) {
        employeeTableBody.innerHTML = "";
    } else {
        for (let reimbursement of employeeRequestsBody) {
            let tableEmployeeRow = document.createElement("tr");
            tableEmployeeRow.innerHTML = `<td>${reimbursement.reimbursementId}</td><td>${reimbursement.employeeId}</td><td>${reimbursement.date}</td><td>${reimbursement.amount}</td><td>${reimbursement.reason}</td><td>${reimbursement.status}</td><td>${reimbursement.comment}</td>`;
            employeeTableBody.appendChild(tableEmployeeRow);
        }
    }
}
