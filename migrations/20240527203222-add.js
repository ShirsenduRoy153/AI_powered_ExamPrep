'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
    async up(queryInterface, Sequelize) {
        // Add the 'limit' column to the 'statuses' table
        await queryInterface.addColumn('statuses', 'limit', {
            type: Sequelize.INTEGER,
            allowNull: false,
            defaultValue: 0, // Default value for the new column
        });
    },

    async down(queryInterface, Sequelize) {
        // Remove the 'limit' column from the 'statuses' table
        await queryInterface.removeColumn('statuses', 'limit');
    }
};