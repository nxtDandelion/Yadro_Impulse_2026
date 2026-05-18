const userId = window.location.pathname.split('/').pop();

async function load_user() {
    const container = document.getElementById('user_container');
    
    try {
        const response = await fetch(`/api/users/${userId}`);
        const user = await response.json();
        
        if (!response.ok) throw new Error('Пользователь не найден');
        
        container.innerHTML = `
            <h2>${user.firstname || ''} ${user.lastname || ''} ${user.fathername || ''}</h2>
            
            <h3>Основная информация</h3>
            <table border="1" cellpadding="8" cellspacing="0">
                <tr><th>ID</th><td>${user.id}</td></tr>
                <tr><th>Имя</th><td>${user.firstname || ''}</td></tr>
                <tr><th>Фамилия</th><td>${user.lastname || ''}</td></tr>
                <tr><th>Отчество</th><td>${user.fathername || ''}</td></tr>
                <tr><th>Возраст</th><td>${user.age || ''}</td></tr>
                <tr><th>Телефон</th><td>${user.phone || ''}</td></tr>
                <tr><th>Email</th><td>${user.email || ''}</td></tr>
                <tr><th>Адрес</th><td>${user.address || ''}</td></tr>
                <tr><th>Пол</th><td>${user.gender || ''}</td></tr>
            </table>
            
            <h3>Паспортные данные</h3>
            <table border="1" cellpadding="8" cellspacing="0">
                <tr><th>Серия и номер паспорта</th><td>${user.passport_num || ''}</td></tr>
                <tr><th>Код подразделения</th><td>${user.passport_code || ''}</td></tr>
                <tr><th>Кем выдан</th><td>${user.passport_otd || ''}</td></tr>
                <tr><th>Дата выдачи</th><td>${user.passport_date || ''}</td></tr>
            </table>
            
            <h3>Налоговая информация</h3>
            <table border="1" cellpadding="8" cellspacing="0">
                <tr><th>ИНН физ.лица</th><td>${user.inn_fiz || ''}</td></tr>
                <tr><th>ИНН юр.лица</th><td>${user.inn_ur || ''}</td></tr>
                <tr><th>СНИЛС</th><td>${user.snils || ''}</td></tr>
                <tr><th>ОМС</th><td>${user.oms || ''}</td></tr>
                <tr><th>ОГРН</th><td>${user.ogrn || ''}</td></tr>
                <tr><th>КПП</th><td>${user.kpp || ''}</td></tr>
            </table>
            
            <h3>Банковские реквизиты</h3>
            <table border="1" cellpadding="8" cellspacing="0">
                <tr><th>БИК банка</th><td>${user.bank_bik || ''}</td></tr>
                <tr><th>Корреспондентский счет</th><td>${user.bank_corr || ''}</td></tr>
                <tr><th>ИНН банка</th><td>${user.bank_inn || ''}</td></tr>
                <tr><th>КПП банка</th><td>${user.bank_kpp || ''}</td></tr>
                <tr><th>Номер счета</th><td>${user.bank_num || ''}</td></tr>
                <tr><th>Имя владельца карты</th><td>${user.bank_client || ''}</td></tr>
                <tr><th>Номер карты</th><td>${user.bank_card || ''}</td></tr>
                <tr><th>Срок действия карты</th><td>${user.bank_date || ''}</td></tr>
                <tr><th>CVC код</th><td>${user.bank_cvc || ''}</td></tr>
            </table>
            
            <h3>Образование</h3>
            <table border="1" cellpadding="8" cellspacing="0">
                <tr><th>Специальность</th><td>${user.edu_spec || ''}</td></tr>
                <tr><th>Направление</th><td>${user.edu_program || ''}</td></tr>
                <tr><th>Учебное заведение</th><td>${user.edu_name || ''}</td></tr>
                <tr><th>Серия и номер диплома</th><td>${user.edu_doc_num || ''}</td></tr>
                <tr><th>Регистрационный номер</th><td>${user.edu_reg_num || ''}</td></tr>
                <tr><th>Дата окончания обучения</th><td>${user.edu_year || ''}</td></tr>
            </table>
            
            <h3>Автомобиль</h3>
            <table border="1" cellpadding="8" cellspacing="0">
                <tr><th>Марка автомобиля</th><td>${user.car_brand || ''}</td></tr>
                <tr><th>Модель автомобиля</th><td>${user.car_model || ''}</td></tr>
                <tr><th>Год выпуска</th><td>${user.car_year || ''}</td></tr>
                <tr><th>Цвет</th><td>${user.car_color || ''}</td></tr>
                <tr><th>Номерной знак</th><td>${user.car_number || ''}</td></tr>
                <tr><th>VIN код</th><td>${user.car_vin || ''}</td></tr>
                <tr><th>Серия и номер СТС</th><td>${user.car_sts || ''}</td></tr>
                <tr><th>Дата выдачи СТС</th><td>${user.car_sts_date || ''}</td></tr>
                <tr><th>Серия и номер ПТС</th><td>${user.car_pts || ''}</td></tr>
                <tr><th>Дата выдачи ПТС</th><td>${user.car_pts_date || ''}</td></tr>
            </table>
        `;
        
    } catch (error) {
        container.innerHTML = 'Ошибка загрузки: ' + error.message;
    }
}

load_user();