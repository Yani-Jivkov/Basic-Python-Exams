airline_name = input()
adult_tickets_sold = int(input())
child_tickets_sold = int(input())
adult_ticket_price = float(input())
service_fee = float(input())

child_ticket_price = adult_ticket_price - (0.7 * adult_ticket_price)
adult_ticket_total_price = adult_ticket_price + service_fee
child_ticket_total_price = child_ticket_price + service_fee
total_profit = (adult_tickets_sold * adult_ticket_total_price) + (child_tickets_sold * child_ticket_total_price)
agency_profit = 0.2 * total_profit

print(f"The profit of your agency from {airline_name} tickets is {agency_profit:.2f} lv.")
