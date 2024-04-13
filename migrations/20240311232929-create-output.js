'use strict';
/** @type {import('sequelize-cli').Migration} */
module.exports = {
    async up(queryInterface, Sequelize) {
        await queryInterface.createTable('outputs', {
            id: {
                allowNull: false,
                autoIncrement: true,
                primaryKey: true,
                type: Sequelize.INTEGER
            },
            linkedlist_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            stack_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            queue_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            tree_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            graph_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            hashing_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            heap_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            sorting_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            searching_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            dynamicprogramming_priority: {
                type: Sequelize.DECIMAL(10, 5)
            },
            chain1: {
                type: Sequelize.DECIMAL(10, 5)
            },
            chain2: {
                type: Sequelize.DECIMAL(10, 5)
            },
            chain3: {
                type: Sequelize.DECIMAL(10, 5)
            },
            chain4: {
                type: Sequelize.DECIMAL(10, 5)
            },
            chain5: {
                type: Sequelize.DECIMAL(10, 5)
            },
            chain6: {
                type: Sequelize.DECIMAL(10, 5)
            },
            createdAt: {
                allowNull: false,
                type: Sequelize.DATE
            },
            updatedAt: {
                allowNull: false,
                type: Sequelize.DATE
            }
        });
    },
    async down(queryInterface, Sequelize) {
        await queryInterface.dropTable('outputs');
    }
};