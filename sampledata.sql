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

INSERT INTO magisair_db.flight_scheduler_booking (booking_no, date, total_cost) VALUES
('B001', '2024-12-01', 350.00),
('B002', '2024-12-02', 420.00),
('B003', '2024-12-03', 580.00),
('B004', '2024-12-04', 150.00),
('B005', '2024-12-05', 275.00);

INSERT INTO magisair_db.flight_scheduler_passenger (passenger_id, name, birth_date, gender) VALUES
('P001', 'Alice Johnson', '1990-01-15', 'Female'),
('P002', 'Bob Smith', '1985-05-22', 'Male'),
('P003', 'Claire Lee', '2000-07-18', 'Female'),
('P004', 'Daniel Brown', '1995-10-10', 'Male'),
('P005', 'Emily Davis', '1988-03-09', 'Female');

INSERT INTO magisair_db.flight_scheduler_crewpersonnel (employee_id, name, phone, email, role) VALUES
('E001', 'John Doe', '123-456-7890', 'johndoe@magisair.com', 'Pilot'),
('E002', 'Sarah Green', '234-567-8901', 'sarahgreen@magisair.com', 'Co-Pilot'),
('E003', 'Michael White', '345-678-9012', 'michaelwhite@magisair.com', 'Flight Attendant'),
('E004', 'Anna Black', '456-789-0123', 'annablack@magisair.com', 'Flight Attendant'),
('E005', 'David Blue', '567-890-1234', NULL, 'Ground Crew');

INSERT INTO magisair_db.flight_scheduler_plane (plane_no, model) VALUES
('PAL001', 'Boeing 747'),
('JAL002', 'Airbus A320'),
('SPRT003', 'Boeing 777'),
('PAL004', 'Embraer 190'),
('CEBU005', 'Airbus A350');


