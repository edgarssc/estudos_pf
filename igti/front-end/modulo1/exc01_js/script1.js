//code solution1();
// function solution1() {
//     let employeesPromise = fetch("http://localhost:3000/employees");

//     employeesPromise.then((resp1) => {
//         resp1.json().then((employees) => {
//             let rolesPromise = fetch("http://localhost:3000/roles");
//             rolesPromise.then((resp2) => {
//                 resp2.json().then((roles) => {
//                     let table = employee_list(employees, roles);
//                     document.getElementById("app").innerHTML = table;
//                 })
//             });
//         });
//     });
// }
//solution1();

//função para retornar um json
function fetchJson(url){
    return fetch(url).then((resp) => {
        if (resp.ok) {
            return resp.json();
        }
        else{
            throw new Error(resp.statusText);
        }
    });
}
//code solução2()
// function solution2() {
//     fetchJson("http://localhost:3000/employees").then((employees) => {
//         fetchJson("http://localhost:3000/roles").then((roles) => {
//             let table = employee_list(employees, roles);
//             document.getElementById("app").innerHTML = table;
//         })
//         .catch(showError);//chama o metodo showError
//     })
//     .catch(showError); //chama o metodo showError

// };
// //solution2();

// function solution3(){
//     Promise.all([
//         fetchJson("http://localhost:3000/employees"),
//         fetchJson("http://localhost:3000/roles"),
//     ]).then(([employees, roles]) => {
//         let table = employee_list(employees, roles);
//         document.getElementById("app").innerHTML = table;
//     }, showError); //chama o metodo showError
// }
// //solution3();

// //codigo solution4();
// async function solution4() {
//     try{
//         let employees = await fetchJson("http://localhost:3000/employees");
//         let roles = await fetchJson("http://localhost:3000/roles");
//         let table = employee_list(employees, roles);
//         document.getElementById("app").innerHTML = table;
//     } 
//     catch(error) {
//         showError();
//     }
// };
//solution4();

//code solution5();
async function solution5() {
    try {
        let [employees, roles] = await Promise.all([
            fetchJson("http://localhost:3000/employees"),
            fetchJson("http://localhost:3000/roles"),
        ]);
            let table = employee_list(employees, roles);
            document.getElementById("app").innerHTML = table;
    }
    catch (console){
        showError();
    } 
    finally { //used when there is a task that always be executed
        console.log("Carregou");
    }
}
solution5();

//Show mensager error
function showError(error) {
    document.getElementById("app").innerHTML = "Erro ao carregar os dados";
    console.error(error);
}

//load all itens of json on screen
function employee_list(employees, roles) {
   let rows = employees.map(employee => {
        let role = roles.find(role => role.id == employee.role_id);
        return `<tr><td>${employee.id}</td><td>${employee.name}</td><td>${role.name}</td></tr>`
    })   
    return `<table>${rows.join("")}</table>`
}