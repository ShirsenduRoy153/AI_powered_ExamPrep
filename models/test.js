'use strict';
const {
    Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
    class test extends Model {
        /**
         * Helper method for defining associations.
         * This method is not a part of Sequelize lifecycle.
         * The `models/index` file will call this method automatically.
         */
        static associate(models) {
            // define association here
        }
    }
    test.init({
        q: DataTypes.STRING,
        o1: DataTypes.STRING,
        o2: DataTypes.STRING,
        o3: DataTypes.STRING,
        o4: DataTypes.STRING,
        a: DataTypes.STRING,
        t: DataTypes.STRING
    }, {
        sequelize,
        modelName: 'test',
    });
    return test;
};