$(document).ready(() => {
    const inputs = $('input')
    const selects = $('select')
    const textarea = $('textarea')

    inputs.addClass('form-control mb-3')
    selects.addClass('form-select mb-3')
    textarea.addClass('form-control mb-3')

    const favButtons = $('.fav-action-btn')
    const baseUrl = 'http://localhost:8000/api/v1'
    const serializeData = array => {
        let result = {}

        for (let item of array) {
            result[item['name']] = item['value']
        }

        return result
    }

    const removeCommentBtn = $('.remove_comment')

    favButtons.on('click', function (e) {
        e.preventDefault();
        const photoId = e.target.dataset.photoId
        const notificationBlock = $(`#notification-${photoId}`)
        const addToFavBtn = $(`#add-to-fav-btn-${photoId}`)
        const rmFromFavBtn = $(`#remove-from-fav-btn-${photoId}`)

        $(this).prop('disabled', true)

        // Имитация времени ожидания выполнения запроса,
        // т.к. Запрос выполняется моментально и не видно что кнопка блокируется
        setTimeout(() => {
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

                    const usersInFavBlock = $('.in-fav-list')

                    if (usersInFavBlock) {
                        usersInFavBlock.empty();

                        $.get(`${baseUrl}/gallery/${photoId}/`).done(res => {
                            for (let user of res['users_in_favourites']) {
                                usersInFavBlock.append(
                                    `<li class="list-group-item"><a href="http://localhost:8000/accounts/${user.id}/profile">${user.username}</a></li>`
                                )
                            }
                        })
                    }
                })
                .always(res => $(this).prop('disabled', false))
        }, 2000)
    })

    $('#comment-form').on('submit', function (e) {
        e.preventDefault();

        const actionUrl = $(this).attr('action')
        const formData = serializeData($(this).serializeArray())
        console.log(actionUrl)
        console.log(formData)

        $.ajax({
            contentType: 'application/json',
            url: actionUrl,
            method: 'post',
            data: JSON.stringify(formData),
            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
        })
            .then(res => {
                $('#comments').prepend(
                    `<div class="card mb-3" id="comment-${res.id}">
                        <div class="card-header">
                            <span>${moment(res['created_at']).format('L')} | ${res['author'].username}</span>
                            <a href="" class="remove_comment" data-comment-id="${res.id}"><i class="far fa-trash-alt"></i></a>
                        </div>
                        <div class="card-body">
                            <blockquote class="blockquote mb-0">
                                <footer class="blockquote-footer">${res.text}</footer>
                            </blockquote>
                        </div>
                    </div>`
                )
            })
            .catch(res => console.log(res))
    })

    removeCommentBtn.on('click', function (e) {
        e.preventDefault();

        const commentId = $(this).data()['commentId']

        $.ajax({
            url: `http://localhost:8000/api/v1/gallery/comments/${commentId}/`,
            method: 'delete',
            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
        })
            .then(res => $(`#comment-${commentId}`).remove())
            .catch(res => console.log(res))
    })

})