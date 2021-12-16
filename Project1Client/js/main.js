const url = "http://127.0.0.1:5000/";

/* Validate manager login credentials and send user to manager home page if validation is successful*/
let button = document.getElementById("manager-login");

async function validateLogin() {
    let username = document.getElementById("manager-username").value;
    let password = document.getElementById("manager-password").value;
    let response = await fetch(url + "manager/login", {method: "POST", headers: {
        "Content-Type": "application/json",
      }, body: JSON.stringify({username, password})});

    if (response.status === 200) {
        let managerId = await response.json()
        transfer(managerId)
    } else {
        alert("Either your username or password or both are incorrect!");
    }
}

function transfer(managerId) {
    sessionStorage.setItem("managerId", managerId.managerId);
    window.location.href="/manager_home.html";
}

/* Return pending requests and dynamically display them when button is clicked */
const table = document.getElementById("table-pending");
const tableBody = document.getElementById("table-body-pending");

async function returnPendingRequests() {

    let response = await fetch(url + "pending");
    let requests = await response.json();
    
    console.log(requests);
    // if (requests.status === 200) {
        populateData(requests);
    // } else {alert("There was a problem returning pending requests.");}
}

function populateData(requestsBody) {
    for (let request of requestsBody) {
        let tableRow = document.createElement("tr");
        tableRow.innerHTML = `<td>${request.reimbursementId}</td><td>${request.employeeId}</td><td>${request.date}</td><td>${request.amount}</td><td>${request.reason}</td><td>${request.status}</td><td>${request.comment}</td>`;
        tableBody.appendChild(tableRow);
    }
}
