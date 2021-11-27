document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#changeProperty').onsubmit = () => {
        let status = document.querySelector("#bugStatus").value;
        let engineer_id = parseInt(document.querySelector("#Engineer").value);
        let bug_id_string = document.querySelector('#Bug_id').innerHTML;
        status.toString();
        bug_id_string.toString();
        let bug_id_list = bug_id_string.split("-");
        let bug_id = parseInt(bug_id_list[1]);

        // location.href = "update/"+engineer_id+"/"+status;
        location.href = "http://127.0.0.1:8000/bug/"+bug_id+"/update/"+engineer_id+"/"+status;

        return false;
    };
});