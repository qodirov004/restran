document.addEventListener('DOMContentLoaded', function() {
    function updatePrice(itemElement) {
        const quantityInput = itemElement.querySelector('.quantity-input');
        const itemPriceElement = itemElement.querySelector('.item-price');
        const basePrice = parseFloat(itemPriceElement.dataset.price);
        const quantity = parseInt(quantityInput.value);
        const updatedPrice = basePrice * quantity;
        itemPriceElement.textContent = updatedPrice.toFixed(2);
    }

    document.querySelectorAll('.quantity-increase').forEach(button => {
        button.addEventListener('click', function() {
            const itemElement = this.closest('.d-flex.align-items-center');
            const quantityInput = itemElement.querySelector('.quantity-input');
            let quantity = parseInt(quantityInput.value);
            quantity += 1;
            quantityInput.value = quantity;
            updatePrice(itemElement);
        });
    });

    document.querySelectorAll('.quantity-decrease').forEach(button => {
        button.addEventListener('click', function() {
            const itemElement = this.closest('.d-flex.align-items-center');
            const quantityInput = itemElement.querySelector('.quantity-input');
            let quantity = parseInt(quantityInput.value);
            if (quantity > 1) {
                quantity -= 1;
                quantityInput.value = quantity;
                updatePrice(itemElement);
            }
        });
    });
});