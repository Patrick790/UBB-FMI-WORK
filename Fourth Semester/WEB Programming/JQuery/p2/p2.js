function validateDate(birthday) {
    let dt2 = new Date(birthday.val());
    return isNaN(dt2);
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
    const name = $("#nameTF")
    const bday = $("#bdayTF");
    const age = $("#ageTF");
    const email = $("#emailTF");

    let errors = "";

    if (!/^[a-zA-Z ]+$/.test(name.val())) {
        errors += "The name field can't contain digits!\n";
        $('#nameTF').css('border-color', 'red');
    } else {
        $('#nameTF').css('border-color', 'green');
    }

    if (validateDate(bday)) {
        errors += "Invalid date!\n";
        $('#bdayTF').css('border-color', 'red');
    } else {
        $('#bdayTF').css('border-color', 'green');
    }

    if(!validateAge(age.val())) {
        errors += "Invalid age!\n";
        $('#ageTF').css('border-color', 'red');
    }
    else {
        $('#ageTF').css('border-color', 'green');
    }




    if (!validateEmail(email.val()) || email.val() == null) {
        errors += "Invalid email!\n";
        $('#emailTF').css('border-color', 'red');
    } else {
        $('#emailTF').css('border-color', 'green');
    }

    if (errors.length > 0) {
        window.alert(errors);
    } else {
        window.alert("All's well!");
    }
}