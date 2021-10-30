$(document).ready(() => {
    const inputs = $('input')
    const selects = $('select')
    const textarea = $('textarea')

    inputs.addClass('form-control mb-3')
    selects.addClass('form-select mb-3')
    textarea.addClass('form-control mb-3')

    const favButtons = $('.fav-action-btn')
    const baseUrl = 'http://localhost:8000/api/v1'

    favButtons.on('click', function (e) {
        e.preventDefault();
        const photoId = e.target.dataset.photoId
        const notificationBlock = $(`#notification-${photoId}`)
        const addToFavBtn = $(`#add-to-fav-btn-${photoId}`)
        const rmFromFavBtn = $(`#remove-from-fav-btn-${photoId}`)

        console.log(addToFavBtn)
        console.log(rmFromFavBtn)

        $.ajax({
            url: `${baseUrl}/${photoId}/favourites_gateway/`,
            method: 'post',
            headers: {'X-CSRFToken': Cookies.get('csrftoken')}
        })
            .done(res => {
                notificationBlock.addClass('alert-success');
                notificationBlock.text(res['detail']);

                setTimeout(() => {
                    notificationBlock.removeClass('alert-success');
                    notificationBlock.text('');
                }, 5000)

                const addBtnStyleProp = addToFavBtn.prop('style')

                if (addBtnStyleProp && addBtnStyleProp['display'] === 'none') {
                    addToFavBtn.show();
                    rmFromFavBtn.hide();
                } else {
                    rmFromFavBtn.show()
                    addToFavBtn.hide();
                }
            })
    })
})