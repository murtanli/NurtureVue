window.onload = function() {
    var passwordInput = document.getElementById("passwordInput");
    var eyeOpenIcon = document.getElementById("eyeOpenIcon");
    var eyeClosedIcon = document.getElementById("eyeClosedIcon");

    var passwordInput2 = document.getElementById("passwordInput2");
    var eyeOpenIcon2 = document.getElementById("eyeOpenIcon2");
    var eyeClosedIcon2 = document.getElementById("eyeClosedIcon2");

    // По умолчанию скрываем пароль
    passwordInput.type = "password";
    eyeOpenIcon.style.display = "inline-block";
    eyeClosedIcon.style.display = "none";

    passwordInput2.type = "password";
    eyeOpenIcon2.style.display = "inline-block";
    eyeClosedIcon2.style.display = "none";

   
}

function togglePasswordVisibility() {
    var passwordInput = document.getElementById("passwordInput");
    var eyeOpenIcon = document.getElementById("eyeOpenIcon");
    var eyeClosedIcon = document.getElementById("eyeClosedIcon");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeOpenIcon.style.display = "none";
        eyeClosedIcon.style.display = "inline-block";

        // Сохраняем состояние видимости пароля в localStorage
        localStorage.setItem("passwordVisibility", "visible");
    } else {
        passwordInput.type = "password";
        eyeOpenIcon.style.display = "inline-block";
        eyeClosedIcon.style.display = "none";

        // Сохраняем состояние видимости пароля в localStorage
        localStorage.setItem("passwordVisibility", "hidden");
    }
}

function togglePasswordVisibility2() {
    var passwordInput = document.getElementById("passwordInput2");
    var eyeOpenIcon = document.getElementById("eyeOpenIcon2");
    var eyeClosedIcon = document.getElementById("eyeClosedIcon2");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeOpenIcon.style.display = "none";
        eyeClosedIcon.style.display = "inline-block";

        // Сохраняем состояние видимости пароля в localStorage
        localStorage.setItem("passwordVisibility", "visible");
    } else {
        passwordInput.type = "password";
        eyeOpenIcon.style.display = "inline-block";
        eyeClosedIcon.style.display = "none";

        // Сохраняем состояние видимости пароля в localStorage
        localStorage.setItem("passwordVisibility", "hidden");
    }
}
