'use strict';

module.exports = {
    up: async(queryInterface, Sequelize) => {
        await queryInterface.renameColumn('statuses', 'linklist', 'linkedlist');
        // ... repeat the process for other columns
    },

    down: async(queryInterface, Sequelize) => {
        await queryInterface.renameColumn('statuses', 'linkedlist', 'linklist');
        // ... repeat the process for other columns
    },
};