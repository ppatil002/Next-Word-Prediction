$("form#submit input").on('keypress', function (event) {
    event.preventDefault();
    if (event.which === 32) {
        $('button.submit').trigger('click');
    }
});

// when space bar is pressed form should be submited