    document.body.onkeyup = function (e) {
    if (e.keyCode == 32) {
        function submitForm() {
            let form = document.getElementById("form1");
            form.submit();
        }
        submitForm();

    }
}

function concattext_with_predicted() {
    var original_text = document.getElementById("text_box").value;
    var predicted_text = document.getElementById("predicted_text").textContent;
    original_text=original_text.trim();
    original_text=original_text.concat(" ");
    predicted_text=predicted_text.trim();
    document.getElementById("text_box").value = original_text.concat(predicted_text);
}

function correct_incorrect_word(){
  var original_text = document.getElementById("text_box").value;
  original_text=original_text.trim();
  var correct_spelling= document.getElementById("correct_spelling").value;
  correct_spelling=correct_spelling.trim();

  var res = original_text.split(" ");
  res.pop();
  original_text=res.join(" ");

  original_text=original_text.concat(" ");
  document.getElementById("text_box").value=original_text.concat(correct_spelling);
}
