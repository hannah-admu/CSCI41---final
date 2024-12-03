INSERT INTO magisair_db.flight_scheduler_destination (city_id, city_name, country, airport) VALUES
('C001', 'New York', 'USA', 'John F. Kennedy International Airport'),
('C002', 'Los Angeles', 'USA', 'Los Angeles International Airport'),
('C003', 'London', 'UK', 'Heathrow Airport'),
('C004', 'Tokyo', 'Japan', 'Narita International Airport'),
('C005', 'Paris', 'France', 'Charles de Gaulle Airport');

INSERT INTO magisair_db.flight_scheduler_route (route_id, departed_city, destination_id, departure_time, arrival_time, expected_travel_time) VALUES
('R001', 'New York', 'C002', '08:00:00', '11:00:00', '03:00:00'),
('R002', 'Los Angeles', 'C003', '09:00:00', '17:00:00', '08:00:00'),
('R003', 'London', 'C004', '10:00:00', '18:30:00', '08:30:00'),
('R004', 'Tokyo', 'C005', '14:00:00', '18:30:00', '04:30:00'),
('R005', 'Paris', 'C001', '06:00:00', '14:30:00', '08:30:00');

INSERT INTO magisair_db.flight_scheduler_crewpersonnel (employee_id, last_name, first_name, middle_initial, phone, email, role) VALUES
('E001', 'Doe', 'John', 'M', '123-456-7890', 'johndoe@magisair.com', 'Pilot'),
('E002', 'Smith', 'Sarah', 'J', '234-567-8901', 'sarahsmith@magisair.com', 'Co-Pilot'),
('E003', 'Brown', 'Michael', 'L', '345-678-9012', 'michaelbrown@magisair.com', 'Flight Attendant'),
('E004', 'White', 'Anna', 'K', '456-789-0123', 'annawhite@magisair.com', 'Flight Attendant'),
('E005', 'Green', 'David', 'P', '567-890-1234', NULL, 'Ground Crew');

INSERT INTO magisair_db.flight_scheduler_flightcrew (crew_id, employee_id) VALUES
('C001', 'E001'),
('C002', 'E002'),
('C003', 'E003'),
('C004', 'E004'),
('C005', 'E005');

INSERT INTO magisair_db.flight_scheduler_plane (plane_no, model) VALUES
('PL001', 'Boeing 747'),
('PL002', 'Airbus A320'),
('PL003', 'Boeing 777'),
('PL004', 'Embraer 190'),
('PL005', 'Airbus A350');

INSERT INTO magisair_db.flight_scheduler_schedule (schedule_id, date) VALUES
('SCHD0001', '2024-12-01'),
('SCHD0002', '2024-12-02'),
('SCHD0003', '2024-12-03'),
('SCHD0004', '2024-12-04'),
('SCHD0005', '2024-12-05');

INSERT INTO magisair_db.flight_scheduler_flight (flight_no, origin, duration, cost, schedule_id) VALUES
('FL001', 'New York', '05:00:00', 350.00, 'SCHD0001'),
('FL002', 'Los Angeles', '06:30:00', 450.00, 'SCHD0002'),
('FL003', 'London', '08:45:00', 600.00, 'SCHD0003'),
('FL004', 'Tokyo', '10:15:00', 800.00, 'SCHD0004'),
('FL005', 'Paris', '07:30:00', 550.00, 'SCHD0005');

INSERT INTO magisair_db.flight_scheduler_passenger (passenger_id, name, birth_date, gender) VALUES
('P001', 'Alice Johnson', '1990-01-15', 'Female'),
('P002', 'Bob Smith', '1985-05-22', 'Male'),
('P003', 'Claire Lee', '2000-07-18', 'Female'),
('P004', 'Daniel Brown', '1995-10-10', 'Male'),
('P005', 'Emily Davis', '1988-03-09', 'Female');

INSERT INTO magisair_db.flight_scheduler_additionalitem (item_no, description, quantity, cost) VALUES
('A001', 'Extra Baggage', 2, 50.00),
('A002', 'Priority Boarding', 1, 20.00),
('A003', 'In-flight Meal', 1, 15.00),
('A004', 'Wi-Fi Access', 1, 10.00),
('A005', 'Extra Legroom', 1, 30.00);

INSERT INTO magisair_db.flight_scheduler_itembilling (billing_id, additional_item_id) VALUES
('BILL001', 'A001'),
('BILL002', 'A002'),
('BILL003', 'A003'),
('BILL004', 'A004'),
('BILL005', 'A005');

INSERT INTO magisair_db.flight_scheduler_booking (booking_no, flight_no_id, item_billing_id, passenger_id, date, total_cost) VALUES
('BKG001', 'FL001', 'BILL001', 'P001', '2024-12-01', 400.00),
('BKG002', 'FL002', 'BILL002', 'P002', '2024-12-02', 470.00),
('BKG003', 'FL003', 'BILL003', 'P003', '2024-12-03', 615.00),
('BKG004', 'FL004', 'BILL004', 'P004', '2024-12-04', 810.00),
('BKG005', 'FL005', 'BILL005', 'P005', '2024-12-05', 580.00);



