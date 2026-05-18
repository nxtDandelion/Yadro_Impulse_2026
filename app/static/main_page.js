let currentPage = 1;
const limit = 25;

async function load_users() {
    const container = document.getElementById('table_container');
    try {
        const response = await fetch(`/api/users?page=${currentPage}&limit=${limit}`);
        const data = await response.json();
        if (!response.ok) throw new Error('Ошибка загрузки');

        if (data.users.length === 0) {
            container.innerHTML = 'Пользователи не найдены';
            return;
        }

        const table = document.createElement('table');
        table.border = "1";
        table.cellPadding = "8";
        table.cellSpacing = "0";

        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');

        const headers = ['Имя', 'Фамилия', 'Телефон', 'Почта', 'Адрес', 'Пол', 'Доп. информация'];
        headers.forEach(headerText => {
            const th = document.createElement('th');
            th.textContent = headerText;
            headerRow.appendChild(th);
        });
        thead.appendChild(headerRow);
        table.appendChild(thead);

        const tbody = document.createElement('tbody');

        data.users.forEach(user => {
            const row = document.createElement('tr');

            const first_name_cell = document.createElement('td');
            first_name_cell.textContent = user.firstname || '';
            row.appendChild(first_name_cell);

            const last_name_cell = document.createElement('td');
            last_name_cell.textContent = user.lastname || '';
            row.appendChild(last_name_cell);

            const phone_cell = document.createElement('td');
            phone_cell.textContent = user.phone || '';
            row.appendChild(phone_cell);

            const email_cell = document.createElement('td');
            email_cell.textContent = user.email || '';
            row.appendChild(email_cell);

            const address_cell = document.createElement('td');
            address_cell.textContent = user.address || '';
            row.appendChild(address_cell);

            const gender_cell = document.createElement('td');
            gender_cell.textContent = user.gender || '';
            row.appendChild(gender_cell);

            const other_cell = document.createElement('td');
            const button = document.createElement('button');
            button.innerText = 'Перейти';
            button.onclick = function(){
                window.location.href = `/${user.id}`;
            }
            other_cell.appendChild(button);
            row.appendChild(other_cell);

            tbody.appendChild(row);
        });

        table.appendChild(tbody);
        container.innerHTML = '';
        container.appendChild(table);

        renderPagination(data);

    } catch (error) {
        container.innerHTML = 'Error loading users: ' + error.message;
    }
}

function renderPagination(data) {
    const container = document.getElementById('table_container');
    const current = data.page;
    const total = data.total_pages;
    
    const paginationDiv = document.createElement('div');
    paginationDiv.style.marginTop = '20px';
    paginationDiv.style.display = 'flex';
    paginationDiv.style.gap = '10px';
    paginationDiv.style.alignItems = 'center';
    paginationDiv.style.flexWrap = 'wrap';
    
    if (data.has_prev) {
        const firstBtn = document.createElement('button');
        firstBtn.textContent = 'Первая';
        firstBtn.onclick = () => goToPage(1);
        paginationDiv.appendChild(firstBtn);
        
        const prevBtn = document.createElement('button');
        prevBtn.textContent = 'Назад';
        prevBtn.onclick = () => goToPage(current - 1);
        paginationDiv.appendChild(prevBtn);
    } else {
        const firstBtn = document.createElement('button');
        firstBtn.textContent = 'Первая';
        firstBtn.disabled = true;
        paginationDiv.appendChild(firstBtn);
        
        const prevBtn = document.createElement('button');
        prevBtn.textContent = 'Назад';
        prevBtn.disabled = true;
        paginationDiv.appendChild(prevBtn);
    }
    
    let startPage = Math.max(1, current - 2);
    let endPage = Math.min(total, current + 2);
    
    if (startPage > 1) {
        const dots = document.createElement('span');
        dots.textContent = '...';
        paginationDiv.appendChild(dots);
    }
    
    for (let i = startPage; i <= endPage; i++) {
        const pageBtn = document.createElement('button');
        pageBtn.textContent = i;
        if (i === current) {
            pageBtn.disabled = true;
        } else {
            pageBtn.onclick = () => goToPage(i);
        }
        paginationDiv.appendChild(pageBtn);
    }
    
    if (endPage < total) {
        const dots = document.createElement('span');
        dots.textContent = '...';
        paginationDiv.appendChild(dots);
    }
    
    if (data.has_next) {
        const nextBtn = document.createElement('button');
        nextBtn.textContent = 'Далее';
        nextBtn.onclick = () => goToPage(current + 1);
        paginationDiv.appendChild(nextBtn);
        
        const lastBtn = document.createElement('button');
        lastBtn.textContent = 'Последняя';
        lastBtn.onclick = () => goToPage(total);
        paginationDiv.appendChild(lastBtn);
    } else {
        const nextBtn = document.createElement('button');
        nextBtn.textContent = 'Далее';
        nextBtn.disabled = true;
        paginationDiv.appendChild(nextBtn);
        
        const lastBtn = document.createElement('button');
        lastBtn.textContent = 'Последняя';
        lastBtn.disabled = true;
        paginationDiv.appendChild(lastBtn);
    }
    
    const info = document.createElement('span');
    info.textContent = `Страница ${current} из ${total} (всего ${data.total} пользователей)`;
    paginationDiv.appendChild(info);
    
    container.appendChild(paginationDiv);
}

function goToPage(page) {
    currentPage = page;
    load_users();
}

async function load_users_API(event) {
    const count_input = document.getElementById('user_count');
    let count = parseInt(count_input.value);
    const button = event.target;
    button.disabled = true;
    try {
        const response = await fetch(`/?count=${count}`, {
            method: 'POST',
        });
        const result = await response.json();
        currentPage = 1;
        await load_users();
    } catch (error){
        alert('Error:' + error.message);
    } finally {
        button.disabled = false;
    }
}

function go_to_random() {
    window.location.href = '/random';
}

load_users();