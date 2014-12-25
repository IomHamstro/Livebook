function reg() {
    jQuery.ajax({
        url: '/registration/',
        type: "POST"
    });
    return false;
}