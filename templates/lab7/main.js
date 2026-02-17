function fillFilmList() {
    fetch('/lab7/rest-api/films/')
    .then(function (data) {
        return data.json();
    })
    .then(function (films) {
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = '';
        
        for (let i = 0; i < films.length; i++) {
            let tr = document.createElement('tr');

            let tdTitle = document.createElement('td');
            let titleRu = document.createElement('span');
            titleRu.className = 'title-ru';
            titleRu.innerText = films[i].title_ru;
            
            tdTitle.appendChild(titleRu);
     
            if (films[i].title && films[i].title !== films[i].title_ru) {
                let titleOriginal = document.createElement('span');
                titleOriginal.className = 'title-original';
                titleOriginal.innerText = films[i].title;
                tdTitle.appendChild(titleOriginal);
            }
            
            let tdYear = document.createElement('td');
            tdYear.innerText = films[i].year;
            
            let tdActions = document.createElement('td');

            let editButton = document.createElement('button'); 
            editButton.className = 'btn btn-edit';
            editButton.innerText = '✏ Редактировать';
            editButton.onclick = function() {
                editFilm(i);
            };

            let deleteButton = document.createElement('button');
            deleteButton.className = 'btn btn-delete';
            deleteButton.innerText = '🗑 Удалить';
            deleteButton.onclick = function() {
                deleteFilm(i, films[i].title_ru);
            };

            tdActions.appendChild(editButton);
            tdActions.appendChild(deleteButton);

            tr.appendChild(tdTitle);
            tr.appendChild(tdYear);
            tr.appendChild(tdActions);

            tbody.appendChild(tr);
        }
    });
}

function deleteFilm(id, title) {
    if (!confirm('Вы точно хотите удалить фильм "' + title + '"?'))
        return;

    fetch(`/lab7/rest-api/films/${id}`, {method: 'DELETE'})
        .then(function () {
            fillFilmList();
        });
}

function editFilm(id) {
    document.getElementById('modal-title').innerText = 'Редактирование фильма';
    
    fetch(`/lab7/rest-api/films/${id}`)
        .then(function (data) {
            return data.json();
        })
        .then(function (film) {
            document.getElementById('id').value = id;
            document.getElementById('title').value = film.title || '';
            document.getElementById('title_ru').value = film.title_ru || '';
            document.getElementById('year').value = film.year || '';
            document.getElementById('description').value = film.description || '';
            showModal();
        });
}

function addFilm() {
    document.getElementById('modal-title').innerText = 'Добавление фильма';
    
  
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title_ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    
    const errorDiv = document.getElementById('error-message');
    if (errorDiv) {
        errorDiv.innerHTML = '';
    }
    
    showModal();
}

function sendFilm() {
    const id = document.getElementById('id').value;
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title_ru').value,
        year: parseInt(document.getElementById('year').value),
        description: document.getElementById('description').value
    };

    if (!film.title && film.title_ru) {
        console.log('Оригинальное название не указано, будет использовано русское');
    }

    const url = id === '' ? '/lab7/rest-api/films/' : `/lab7/rest-api/films/${id}`;
    const method = id === '' ? 'POST' : 'PUT';

    fetch(url, {
        method: method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(film)
    }).then(function(resp) {
        if (resp.ok) {
            fillFilmList();
            hideModal();
        } else {
            resp.json().then(errorData => {
                const errorDiv = document.getElementById('error-message');
                if (errorDiv) {
                    errorDiv.innerHTML = errorData.description || errorData.error || 'Произошла ошибка';
                }
                console.error('Ошибка сервера:', errorData);
            });
        }
    }).catch(error => {
        console.error('Ошибка сети:', error);
        const errorDiv = document.getElementById('error-message');
        if (errorDiv) {
            errorDiv.innerHTML = 'Ошибка соединения с сервером';
        }
    });
}

function showModal() {
    const errorDiv = document.getElementById('error-message');
    if (errorDiv) {
        errorDiv.innerHTML = '';
    }
    
    document.getElementById('modal').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}

function hideModal() {
    document.getElementById('modal').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';

    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title_ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    
    const errorDiv = document.getElementById('error-message');
    if (errorDiv) {
        errorDiv.innerHTML = '';
    }
}

document.addEventListener('DOMContentLoaded', fillFilmList);
