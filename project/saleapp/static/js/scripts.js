function addTicket(seat_name, flight_id, seat_type_id, price, plane_id) {
    let count_seat = parseInt(document.getElementById('count_seat').value);
    fetch('/add_ticket', {
        method: 'post',
        body: JSON.stringify({
            flight_id,
            plane_id,
            seat_type_id,
            count_seat,
            price,
            seat_name,
        }),
        headers: {
            'Context-Type': 'application/json',
        },
    })
        .then((res) => res.json())
        .then((data) => {
            location.href = '/seat-selection';
        })
        .catch((err) => {
            console.log(err);
        });
}

function check_number_input() {
    input = document.getElementById('count_seat');
    if (parseInt(input.value) < 1) input.value = 1;
}

function checkSeat(context, maxSeat) {
    if (context.className.indexOf('danger') >= 0) {
        context.classList.toggle('danger');
        return;
    }

    btn = document.querySelectorAll('#checkSeat button.danger');
    if (btn.length == maxSeat)
        alert('You have full seat!! Can not be more >.>');
    else context.classList.toggle('danger');
}

function commit(totalSeat) {
    btn = document.querySelectorAll('#checkSeat button.danger');
    if (btn.length !== totalSeat) {
        alert(`You have to select ${totalSeat} seat >.>`);
        return;
    }

    let payment = '';
    let position = '';
    let seat = document.querySelectorAll('button.danger');
    let node = document.querySelectorAll('input.payment-method');

    seat.forEach((e) => {
        if (position !== '') position += ',';
        position += e.getAttribute('data');
    });
    node.forEach((e) => {
        if (e.checked) payment = e.value;
    });

    fetch('/payment', {
        method: 'post',
        body: JSON.stringify({
            payment,
            position,
        }),
        headers: {
            'Context-Type': 'application/json',
        },
    })
    .then(res=>{
        location.href = '/payment'
    })
    .catch((err) => {
        console.log(err);
    });
}
