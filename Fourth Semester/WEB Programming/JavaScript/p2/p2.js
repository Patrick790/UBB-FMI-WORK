function validateDate(birthday) {
    let dt1 = new Date();
    let dt2 = new Date(birthday.value.toString());
    return !(dt2 < dt1);
}

function validateAge(age) {
    if (age === '')
        return false;
    const regAge = /^[0-9]+$/;
    return regAge.test(age);
}

function validateEmail(email) {
    return String(email)
        .toLowerCase()
        .match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
}


function validate() {
    const name = document.getElementById("nameTF");
    const bday = document.getElementById("bdayTF");
    const age = document.getElementById("ageTF");
    const email = document.getElementById("emailTF");

    let errors = "";

    if (!/^[a-zA-Z ]+$/.test(name.value)) {
        errors += "The name field can't contain digits!\n";
        name.style.borderColor = "red";
    } else {
        name.style.borderColor = "green";
    }

    if (validateDate(bday)) {
        errors += "Invalid date!\n";
        bday.style.borderColor = "red";
    } else {
        bday.style.borderColor = "green";
    }

    if(!validateAge(age.value)) {
        errors += "Invalid age!\n";
        age.style.borderColor = "red";
    }
    else {
        age.style.borderColor = "green";
    }




    if (!validateEmail(email.value) || email.value == null) {
        errors += "Invalid email!\n";
        email.style.borderColor = "red";
    } else {
        email.style.borderColor = "green";
    }

    if (errors.length > 0) {
        window.alert(errors);
    } else {
        window.alert("All's well!");
    }
}