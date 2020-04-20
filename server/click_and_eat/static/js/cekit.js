function cePreviewImage(input, id, a) {
    if (input.files && input.files[0]) {
        let reader = new FileReader();

        reader.onload = function (e) {
            $(id).attr(a, e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}