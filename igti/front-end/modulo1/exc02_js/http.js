//função para retornar um json
function fetchJson(url, option){
    return fetch(url, option).then((resp) => {
        if (resp.ok) {
            return resp.json();
        }
        else{
            throw new Error(resp.statusText);
        }
    });
}

function listEmployees() {
    return fetchJson("http://localhost:3000/employees");
}

function listRoles() {
    return fetchJson("http://localhost:3000/roles");
}

function updateEmployee(id, employee) {
// update
return fetchJson(`http://localhost:3000/employees/${id}`,{
    method: 'PUT',
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(employee)
});
}

// create
function createEmployee(employee) {
return fetchJson(`http://localhost:3000/employees`,{
    method: 'POST',
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(employee)
});
}

//code init();
async function init() {
    try {
        [employees, roles] = await Promise.all([listEmployees(), listRoles()]);
        renderRoles();
        renderData();
        clearSelection();
        bcancel.addEventListener("click", clearSelection);
        formEl.addEventListener("submit", onSubmit);
    }
    catch (error){
        showError("Error loading data", error);
    } 
    finally { //used when there is a task that always be executed
        console.log("Carregou");
    }
}
init();

// // delete
// fetch(`http://localhost:3000/employees/${id}`,{
//     method: 'DELETE',
// });



