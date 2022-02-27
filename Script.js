document.body.onkeyup = function(e){
  if(e.keyCode == 32){
      function submitForm() {
          let form = document.getElementById("form1");
          form.submit();
      }
      submitForm();
      
  }
}
