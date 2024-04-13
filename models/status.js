'use strict';
const {
    Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
    class status extends Model {
        /**
         * Helper method for defining associations.
         * This method is not a part of Sequelize lifecycle.
         * The `models/index` file will call this method automatically.
         */
        static associate(models) {
            // define association here
        }
    }
    status.init({
        currenttopic: DataTypes.STRING,
        currentscore: DataTypes.INTEGER,
        linkedlist: DataTypes.INTEGER,
        stack: DataTypes.INTEGER,
        queue: DataTypes.INTEGER,
        tree: DataTypes.INTEGER,
        graph: DataTypes.INTEGER,
        hashing: DataTypes.INTEGER,
        heap: DataTypes.INTEGER,
        sorting: DataTypes.INTEGER,
        searching: DataTypes.INTEGER,
        dynamicprogramming: DataTypes.INTEGER,
        linkedlist_time: DataTypes.DECIMAL(10, 5),
        stack_time: DataTypes.DECIMAL(10, 5),
        queue_time: DataTypes.DECIMAL(10, 5),
        tree_time: DataTypes.DECIMAL(10, 5),
        graph_time: DataTypes.DECIMAL(10, 5),
        hashing_time: DataTypes.DECIMAL(10, 5),
        heap_time: DataTypes.DECIMAL(10, 5),
        sorting_time: DataTypes.DECIMAL(10, 5),
        searching_time: DataTypes.DECIMAL(10, 5),
        dynamicprogramming_time: DataTypes.DECIMAL(10, 5),
        linkedlist_rating: DataTypes.INTEGER,
        stack_rating: DataTypes.INTEGER,
        queue_rating: DataTypes.INTEGER,
        tree_rating: DataTypes.INTEGER,
        graph_rating: DataTypes.INTEGER,
        hashing_rating: DataTypes.INTEGER,
        heap_rating: DataTypes.INTEGER,
        sorting_rating: DataTypes.INTEGER,
        searching_rating: DataTypes.INTEGER,
        dynamicprogramming_rating: DataTypes.INTEGER,
        linkedlist_priority: DataTypes.DECIMAL(10, 5),
        stack_priority: DataTypes.DECIMAL(10, 5),
        queue_priority: DataTypes.DECIMAL(10, 5),
        tree_priority: DataTypes.DECIMAL(10, 5),
        graph_priority: DataTypes.DECIMAL(10, 5),
        hashing_priority: DataTypes.DECIMAL(10, 5),
        heap_priority: DataTypes.DECIMAL(10, 5),
        sorting_priority: DataTypes.DECIMAL(10, 5),
        searching_priority: DataTypes.DECIMAL(10, 5),
        dynamicprogramming_priority: DataTypes.DECIMAL(10, 5)
    }, {
        sequelize,
        modelName: 'status',
    });
    return status;
};