function confirmSubmitAction() {
    // Check if all actions (fire, strap, weight) are confirmed
    var fireConfirmation = localStorage.getItem('fireConfirmation')
    var strapConfirmation = localStorage.getItem('strapConfirmation')
    var weightConfirmation = localStorage.getItem('weightConfirmation')

    // Check if any action is not confirmed
    if (fireConfirmation !== 'confirmed' || strapConfirmation !== 'confirmed' || weightConfirmation !== 'confirmed') {
        // If any action is not confirmed, set submit action to unconfirmed and return
        localStorage.setItem('submitConfirmation', 'unconfirmed')
        updateSlot('submit', 'unconfirmed') // Update the slot immediately
        return
    }

    // If all actions are confirmed, set confirmation flag for submit action in localStorage
    localStorage.setItem('submitConfirmation', 'confirmed')

    // Update progress bar
    updateProgressBar()
    var submitConfirmation = localStorage.getItem('submitConfirmation') // Retrieve the updated confirmation status
    updateSlot('submit', submitConfirmation) // Update the slot accordingly
}

function updateSlot(action, confirmationStatus) {
    var slot = document.getElementById('progress-slot-' + action)
    if (confirmationStatus === 'confirmed') {
        slot.classList.add('progress-filled')
    } else {
        slot.classList.remove('progress-filled')
    }
}

function confirmSelectAction() {
    // Set confirmation flag for select action in localStorage
    localStorage.setItem('selectConfirmation', 'confirmed')
}

function updateProgressBar() {
    // Retrieve confirmation status for each action from localStorage
    var fireConfirmation = localStorage.getItem('fireConfirmation')
    var strapConfirmation = localStorage.getItem('strapConfirmation')
    var weightConfirmation = localStorage.getItem('weightConfirmation')
    var selectConfirmation = localStorage.getItem('selectConfirmation')
    var submitConfirmation = localStorage.getItem('submitConfirmation')

    // Update the progress slots based on confirmation status
    updateSlot('fire', fireConfirmation)
    updateSlot('strap', strapConfirmation)
    updateSlot('weight', weightConfirmation)
    updateSlot('select', selectConfirmation)
    updateSlot('submit', submitConfirmation)
}