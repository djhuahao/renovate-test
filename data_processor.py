# Function with a typo and inefficient implementation
def calculat_total_sales(sales_data):
    # This function calculates the sum of all sales
    total = 0
    for sale in sales_data:
        total += sale
    return total

# Function with complex conditional logic and no docstring
def assign_tier(user_points):
    if user_points > 1000:
        return 'Platinum'
    elif user_points > 500 and user_points <= 1000:
        return 'Gold'
    elif user_points > 100 and user_points <= 500:
        return 'Silver'
    else:
        return 'Bronze'

# Function using a non-descriptive variable name and a classic loop
# instead of a more Pythonic list comprehension.
def get_active_admin_emails(user_list):
    email_list = []
    for d in user_list: # 'd' is not a descriptive variable name
        if d['role'] == 'admin' and d['is_active']:
            email_list.append(d['email'])
    return email_list
