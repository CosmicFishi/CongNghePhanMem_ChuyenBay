function addTicket(){
    
}

flight_id = str(data.get('flight_id'));
customer_id = current_user.id;
seat_type_id = data.get('seat_type_id');
count_seat = data.get('count_seat');
price = data.get('price');
id = flight_id + seat_type_id;

ticket[id] = {
    id: id,
    flight_id: flight_id,
    customer_id: customer_id,
    seat_type_id: seat_type_id,
    count_seat: count_seat,
    price: price,
};