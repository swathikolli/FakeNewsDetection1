let fakenewsFormEl = document.getElementById("fakeNewsDetectionForm");

let titleEl = document.getElementById("tileName");
let titleErrMsgEl = document.getElementById("titleErrMsg");

let DescriptionEl = document.getElementById("descriptionBody");
let DescriptionErrMsgEl = document.getElementById("textErrMsg");

let errorMsg = "Required*";

titleEl.addEventListener("blur", function(event) {
    if (event.target.value === "") {
        titleErrMsgEl.textContent = errorMsg;
    } else {
        titleErrMsgEl.textContent = "";
    }
});

DescriptionEl.addEventListener("blur", function(event) {
    if (event.target.value === "") {
        DescriptionErrMsgEl.textContent = errorMsg;
    } else {
        DescriptionErrMsgEl.textContent = "";
    }
});

fakenewsFormEl.addEventListener("submit", function(event) {
    event.preventDefault();
});