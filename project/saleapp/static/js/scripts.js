function addTicket(
    seat_name,
    flight_id,
    seat_type_id,
    price,
    plane_id,
    total_flight_time,
    time_to_start,
    time_end
) {
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
            localStorage.setItem(
                'ticket',
                JSON.stringify({
                    total_flight_time,
                    time_to_start,
                    time_end,
                })
            );
            if (data.status === 200) location.href = '/seat-selection';
            else {
                location.href = '/fill-info';
            }
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
        .then((res) => {
            location.href = '/payment';
        })
        .catch((err) => {
            console.log(err);
        });
}
function handleCommit(
    nameFrom,
    nameTo,
    phaneId,
    seatName,
    payMethod,
    flight_id,
    seat_type_id,
    count_seat,
    price,
    position
) {
    flight = {
        nameFrom,
        nameTo,
        phaneId,
        seatName,
        payMethod,
        flight_id,
        seat_type_id,
        count_seat,
        price,
        position,
    };
    let baseUrl = `http://api.qrserver.com/v1/create-qr-code/?data=${flight_id},${seat_type_id},${position},${count_seat},${price}&size=200x200`;
    if (payMethod === 'momo') {
        fetch('/momo-pay', {
            method: 'post',
            headers: {
                'Context-Type': 'application/json',
            },
        })
            .then((res) => res.json())
            .then((data) => {
                if (data.mess) {
                    alert(mess);
                    return;
                }
                location.href = data.link;
            })
            .catch((err) => {
                console.log(err);
            });
    } else if (payMethod === 'airport') {
        let ticket = JSON.parse(localStorage.getItem('ticket'));
        ticket = { ...flight, ...ticket };
        localStorage.setItem('ticket', JSON.stringify(ticket));
        localStorage.setItem('qrcode', baseUrl);
        location.href = '/book-history';
    } else {
        alert('Data is not correctly, plz book from start!!!');
    }
}

function loadLocal() {
    flight = JSON.parse(localStorage.getItem('ticket'));
    qrcode = localStorage.getItem('qrcode');
    document.getElementById(
        'add-ticket'
    ).innerHTML = `<div class="card book-card">
                <div class="card-body">
                    <h5 class="card-title"><i class="fas fa-plane"></i> Flight ID: ${flight.flight_id} <button type="button" class="btn btn-primary float-right" data-toggle="modal" data-target="#exampleModal">Payment required</button></h5>
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                        <div class="d-flex flex-wrap">
                            <p class="mb-0 col-md-6 col-sm-12"><strong><i class="fas fa-plane-arrival"></i> Flight to: </strong>${flight.nameFrom}</p>
                            <p class="mb-0 col-md-6 col-sm-12" ><strong><i class="fas fa-plane-departure"></i>  Flight from:</strong>${flight.nameTo}</p>
                        </div>
                        <hr class="my-4">
                        <div class="d-flex flex-wrap">
                            <p class="mb-0 col-md-6 col-sm-12" ><strong><i class="fas fa-clock"></i> Flight start:</strong> ${flight.time_to_start}</p>
                            <p class="mb-0 col-md-6 col-sm-12" ><strong><i class="fas fa-plane"></i> Flight time:</strong> ${flight.total_flight_time}</p>
                        </div>
                        <hr class="my-4">
                        <div class="d-flex flex-wrap">
                            <p class="mb-0 col-md-6 col-sm-12" ><strong><i class="fas fa-suitcase-rolling"></i> Seat type:</strong> ${flight.seatName}</p>
                            <p class="mb-0 col-md-6 col-sm-12" ><strong><i class="fas fa-suitcase-rolling"></i> Seat position:</strong> ${flight.position}</p>
                        </div>
                    </li>
                    </ul>
            </div>
            <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">QR code: </h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                        <div class="modal-body text-center pb-2">
                            <img src='${qrcode}'  alt='qrcode' />
                        </div>
                    </div>
                </div>
            </div>
            `;
}

function addTicketByStaff(seat_name, flight_id, seat_type_id, price, plane_id) {
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
            location.href = '/staff-seat-selection';
        })
        .catch((err) => {
            console.log(err);
        });
}

function staffCommit(totalSeat) {
    btn = document.querySelectorAll('#checkSeat button.danger');
    if (btn.length !== totalSeat) {
        alert(`You have to select ${totalSeat} seat >.>`);
        return;
    }

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

    fetch('/staff-pay', {
        method: 'post',
        body: JSON.stringify({
            position,
        }),
        headers: {
            'Context-Type': 'application/json',
        },
    })
        .then((res) => res.json())
        .then((res) => {
            alert(res.mess);
            if (res.status === 200) location.href = '/staff-book';
            else location.href = '/staff-book';
        })
        .catch((err) => {
            console.log(err);
        });
}
function checkSeatUsed(used = '') {
    btn = document.querySelectorAll('#checkSeat button');
    btn.forEach((e) => {
        if (used.indexOf(e.textContent.trim()) >= 0) {
            e.setAttribute('class', 'btn btn-warning');
            e.setAttribute('disabled', 'true');
        }
    });
}