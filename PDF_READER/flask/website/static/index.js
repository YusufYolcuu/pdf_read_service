$(document).on('change', '.file-input', function() {
    
    console.log("fdf")
    var filesCount = $(this)[0].files.length;
    
    var textbox = $(this).prev();
  
    if (filesCount === 1) {
      var fileName = $(this).val().split('\\').pop();
      textbox.text(fileName);
    } else {
      textbox.text(filesCount + ' files selected');
    }
    console.log(textbox)
});