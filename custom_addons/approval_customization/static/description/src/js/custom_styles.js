odoo.define('approval_customization.custom_styles', function (require) {
    "use strict";

    const ListView = require('web.ListView');
    const core = require('web.core');
    const _t = core._t;

    ListView.include({
        /**
         * Override to add custom logic for applying styles
         */
        _renderRow: function (record, options) {
            const $row = this._super(record, options);
            const receiptState = record.get('receipt_state');

            if (receiptState === 'waiting') {
                $row.find('td.o_purchase_order_state').addClass('o_purchase_order_state_waiting');
                
            } else if (receiptState === 'all_received') {
                $row.find('td.o_purchase_order_state').addClass('o_purchase_order_state_all_received');
            }

            return $row;
        }
    });
});
