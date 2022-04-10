// var today = new Date();
// var dd = today.getDate();
// var mm = today.getMonth() + 1; //January is 0!
// var yyyy = today.getFullYear() - 18;
// if (dd < 10) {
//   dd = "0" + dd;
// }
// if (mm < 10) {
//   mm = "0" + mm;
// }

// today = yyyy + "-" + mm + "-" + dd;
// document.getElementById("txtDOB").setAttribute("max", today);

// $(document).on("keypress", "#phone", function (e) {
//   // e.preventDefault();
//   var titleElement = document.getElementById("phone");
//   console.log("this is a ", e);
//   if (e.target.value.length === 10) {
//     e.preventDefault();
//   }
// });

function numberOnly(id) {
  // Get element by id which passed as parameter within HTML element event
  var element = document.getElementById(id);
  // This removes any other character but numbers as entered by user
  element.value = element.value.replace(/[^0-9]/gi, "");
}

$(document).on("keypress", "#GAAI", function (e) {
  // e.preventDefault();
  var titleElement = document.getElementById("GAAI");
  console.log("this is a ", e);
  if (e.target.value.length === 10) {
    e.preventDefault();
  }
});

initMultiStepForm();

function initMultiStepForm() {
  const progressNumber = document.querySelectorAll(".step").length;
  const slidePage = document.querySelector(".slide-page");
  const submitBtn = document.querySelector(".submit");
  const progressText = document.querySelectorAll(".step p");
  const progressCheck = document.querySelectorAll(".step .check");
  const bullet = document.querySelectorAll(".step .bullet");
  const pages = document.querySelectorAll(".page");
  const nextButtons = document.querySelectorAll(".next");
  const prevButtons = document.querySelectorAll(".prev");
  const stepsNumber = pages.length;

  if (progressNumber !== stepsNumber) {
    alert(
      "Error, number of steps in progress bar do not match number of pages"
    );
  }

  document.documentElement.style.setProperty("--stepNumber", stepsNumber);

  let current = 1;

  for (let i = 0; i < nextButtons.length; i++) {
    nextButtons[i].addEventListener("click", function (event) {
      event.preventDefault();

      inputsValid = validateInputs(this);
      // inputsValid = true;

      if (inputsValid) {
        slidePage.style.marginLeft = `-${(100 / stepsNumber) * current}%`;
        bullet[current - 1].classList.add("active");
        progressCheck[current - 1].classList.add("active");
        // progressText[current - 1].classList.add("active");
        current += 1;
      }
    });
  }

  for (let i = 0; i < prevButtons.length; i++) {
    prevButtons[i].addEventListener("click", function (event) {
      event.preventDefault();
      slidePage.style.marginLeft = `-${(100 / stepsNumber) * (current - 2)}%`;
      bullet[current - 2].classList.remove("active");
      progressCheck[current - 2].classList.remove("active");
      progressText[current - 2].classList.remove("active");
      current -= 1;
    });
  }
  submitBtn.addEventListener("click", function () {
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    progressText[current - 1].classList.add("active");
    current += 1;
    setTimeout(function () {
      alert("Your Form Successfully Signed up");
      location.reload();
    }, 800);
  });

  function validateInputs(ths) {
    let inputsValid = true;

    const inputs = ths.parentElement.parentElement.querySelectorAll("input");
    // const inputss = ths
    for (let i = 0; i < inputs.length; i++) {
      const valid = inputs[i].checkValidity();

      if (!valid) {
        inputsValid = false;
        inputs[i].classList.add("invalid-input");
      } else {
        inputs[i].classList.remove("invalid-input");
      }
    }
    return inputsValid;
  }
}

// $(document).on("keypress", "#id_password", function (e) {
//   var res;
//   var str = document.getElementById("id_password").value;
//   if (
//     str.match(/[a-z]/g) &&
//     str.match(/[A-Z]/g) &&
//     str.match(/[0-9]/g) &&
//     str.match(/[^a-zA-Z\d]/g) &&
//     str.length >= 8
//   ) {
//     res = "TRUE";
//     document.getElementById("submit").disabled = false;
//   } else {
//     res = "FALSE";
//     document.getElementById("t2").value = res;
//   }
//   console.log(res, "this");
// });

function test_str() {
  // e.preventDefault();
  var str = document.getElementById("id_password").value;
  if (
    str.match(/[a-z]/g) &&
    str.match(/[A-Z]/g) &&
    str.match(/[0-9]/g) &&
    str.match(/[^a-zA-Z\d]/g) &&
    str.length >= 8
  ) {
    res = "TRUE";
    document.getElementById("submit").disabled = false;
  } else {
    res = "FALSE";
    // document.getElementById("t2").value = res;
    document.getElementById("submit").disabled = true;
  }
  console.log(res, "this");
}
