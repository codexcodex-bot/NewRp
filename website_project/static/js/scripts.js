document.addEventListener('DOMContentLoaded', (event) => {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-button');
    const removeFromCartButtons = document.querySelectorAll('.remove-from-cart-button');
    const checkoutButton = document.querySelector('#checkoutButton');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const productId = event.target.dataset.productId;
            addToCart(productId);
        });
    });

    removeFromCartButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const productId = event.target.dataset.productId;
            removeFromCart(productId);
        });
    });

    if (checkoutButton) {
        checkoutButton.addEventListener('click', (event) => {
            placeOrder();
        });
    }
});

function addToCart(productId) {
    fetch(`/add_to_cart/${productId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Product added to cart successfully!');
        } else {
            alert('There was an error adding the product to the cart.');
        }
    });
}

function removeFromCart(productId) {
    fetch(`/remove_from_cart/${productId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Product removed from cart successfully!');
        } else {
            alert('There was an error removing the product from the cart.');
        }
    });
}

function placeOrder() {
    fetch('/place_order', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Order placed successfully!');
        } else {
            alert('There was an error placing the order.');
        }
    });
}