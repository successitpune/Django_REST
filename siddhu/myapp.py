import requests

URL = "http://127.0.0.1:8000/customerapi/"  # Replace with your actual Django API endpoint

def get_data(id=None):
    try:
        if id is not None:
            url = f"{URL}{id}/"
        else:
            url = URL
        
        r = requests.get(url)
        r.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        if r.status_code == 200:
            data = r.json()
            if id:
                print(f"Customer with id={id}:")
            else:
                print("All customers:")
            print(data)
        else:
            print("Failed to fetch data. Status code:", r.status_code)
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

def post_data(customer_data):
    try:
        r = requests.post(url=URL, json=customer_data)  # Use json=customer_data for automatic serialization
        r.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        if r.status_code == 201:
            response_data = r.json()
            print("Customer data posted successfully. Response:", response_data)
        else:
            print("Failed to post customer data. Status code:", r.status_code)
            print("Error response:", r.text)  # Print detailed error response for debugging
    except requests.exceptions.RequestException as e:
        print("Error posting customer data:", e)

def update_data(id, updated_data):
    try:
        update_url = f"{URL}{id}/"
        r = requests.put(url=update_url, json=updated_data)
        r.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        if r.status_code == 200:
            response_data = r.json()
            print(f"Customer with id={id} updated successfully. Response:", response_data)
        else:
            print(f"Failed to update customer with id={id}. Status code:", r.status_code)
            print("Error response:", r.text)  # Print detailed error response for debugging
    except requests.exceptions.RequestException as e:
        print(f"Error updating customer with id={id}:", e)

def delete_data(id):
    try:
        delete_url = f"{URL}{id}/"
        r = requests.delete(url=delete_url)
        r.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        if r.status_code == 204:
            print(f"Customer with id={id} deleted successfully.")
        else:
            print(f"Failed to delete customer with id={id}. Status code:", r.status_code)
            print("Error response:", r.text)  # Print detailed error response for debugging
    except requests.exceptions.RequestException as e:
        print(f"Error deleting customer with id={id}:", e)

# Example usage:

if __name__ == "__main__":
    # Fetch all customers
    get_data()

    # Fetch customer with id=1
    get_data(id=1)

    # Example customer data to post
    customer_data = {
        'customer_name': 'John Doe',
        'contact_no': '1234567890',
        'address': '123 Main St, City',
        'company_name': 'Tech Inc',
        'model_no': 'Model X',
        'physical_condition': 'Good',
        'estimated_price': '1000.00',
        'imei_1': '123456789012345',
        'imei_2': '987654321098765',
        'date': '2024-06-16'
    }

    # Post customer data
    post_data(customer_data)

    # Example customer data to update (assuming id=1 exists)
    updated_customer_data = {
        'customer_name': 'Updated John Doe',
        'contact_no': '9876543210',
        'address': '456 Oak St, New City',
        'company_name': 'Updated Tech Inc',
        'model_no': 'Model Y',
        'physical_condition': 'Fair',
        'estimated_price': '1500.00',
        'imei_1': '543216789012345',
        'imei_2': '789654321098765',
        'date': '2024-06-17'
    }

    # Update customer with id=1
    update_data(id=1, updated_data=updated_customer_data)

    # Delete customer with id=1
    delete_data(id=1)
