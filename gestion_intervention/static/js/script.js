$(function () {

    // ==================== DYNAMIC SEARCH ===================// 

    var customerInput = $("#myCustomerInput"); // SEARCH INPUT
    var customerName = $(".customerName"); // LIST ITEMS

    // Hide list items that do not match the input
    customerInput.keyup(function () {
        var filter = customerInput.val().toUpperCase();
        for (i = 0; i < customerName.length; i++) {
            if (filter) {
                if (customerName[i].innerText.toUpperCase().indexOf(filter) >= 0) {
                    customerName[i].style.display = "";
                } else {
                    customerName[i].style.display = "none";
                }
            } else {
                customerName[i].style.display = "";
            }
        }
    });



    // ==================== ADD SPACE BEETWEEN NUMBER IN PHONE NUMBERS ===================// 

    var phone_number = $('.phone_number');


    for (var i = 0; i < phone_number.length; i++) {
        var phone = phone_number[i];
        var phone_text = $(phone).text();
        var phone_modify = phone_text.replace(/(?!^)(?=(?:\d{2})+(?:\.|$))/gm, ' ');
        $(phone).text(phone_modify)
    }



})