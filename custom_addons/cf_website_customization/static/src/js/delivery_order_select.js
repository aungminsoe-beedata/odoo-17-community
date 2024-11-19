/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.websiteSaleDelivery = publicWidget.registry.websiteSaleDelivery.extend({
    start: async function () {
        this._super(...arguments);
        this._bindEvents();
    },
    
    _bindEvents: function() {
        // Consolidate event bindings to reduce memory usage
        $(document).on('click', '.dynamic-button', this._onButtonClick.bind(this));
        $(document).on('click', '.list-group-item', this._onLiClick.bind(this));
    },

    _onButtonClick: function(event) {
        const buttonId = event.currentTarget.id;

        // Reset button styles
        $('.dynamic-button').css({ backgroundColor: '', color: '' });

        // Set clicked button styles
        $(event.currentTarget).css({ backgroundColor: '#60bf1b', color: '#070707' });

        // Show corresponding list item, hide others
        $('.list-group-item').each(function() {
            this.style.display = (this.id === buttonId) ? 'block' : 'none';
        });
    },

    _onLiClick: function(event) {
        // Reset background color for list items
        $('.list-group-item').css('background-color', '');

        // Optionally do something with the clicked item (e.g., apply styles)
        $(event.currentTarget).css('background-color', '');
    },
});
