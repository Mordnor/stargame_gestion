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
    // ==================== END DYNAMIC SEARCH ===================// 

})