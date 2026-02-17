booking_count = 0
total_seats = 10
rejected_count = 0
total_bookings = 0
while True:
  number_of_tickets = int(input("Enter number of Tickets: "))
  if total_seats - booking_count >= number_of_tickets:
    if number_of_tickets <= 15 and number_of_tickets > 0:
      total_bookings += 1
      for i in range(number_of_tickets):
        age = int(input("Enter age of the person: "))
        if age >=12 and age <= 100 :
          booking_count += number_of_tickets
          temp = number_of_tickets
          number_of_tickets = 0
        if age < 12 :
          print("Booking rejected due to age restriction")
          print("Number of tickets=", number_of_tickets)
          rejected_count += 1
          booking_count -= temp
          break
        # confirmed_count += 1
    elif number_of_tickets == 0:
      print(f"Total Bookings: {total_bookings - rejected_count}, Total tickets sold: {booking_count}, rejection count: {rejected_count}, Remaining seats: {total_seats-booking_count} ")
      break
  else:
    print(f"Available tickets are less i.e,{total_seats - booking_count}")
    continue
  print("Booking Successful")
  print(f"Total Bookings: {total_bookings - rejected_count}, Total tickets sold: {booking_count}, rejection count: {rejected_count}, Remaining seats: {total_seats-booking_count} ")
  if booking_count == total_seats:
    print("House Full")
    break