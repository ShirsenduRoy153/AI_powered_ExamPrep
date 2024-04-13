'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class output extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  output.init({
    linkedlist_priority: DataTypes.DECIMAL,
    stack_priority: DataTypes.DECIMAL,
    queue_priority: DataTypes.DECIMAL,
    tree_priority: DataTypes.DECIMAL,
    graph_priority: DataTypes.DECIMAL,
    hashing_priority: DataTypes.DECIMAL,
    heap_priority: DataTypes.DECIMAL,
    sorting_priority: DataTypes.DECIMAL,
    searching_priority: DataTypes.DECIMAL,
    dynamicprogramming_priority: DataTypes.DECIMAL,
    chain1: DataTypes.DECIMAL,
    chain2: DataTypes.DECIMAL,
    chain3: DataTypes.DECIMAL,
    chain4: DataTypes.DECIMAL,
    chain5: DataTypes.DECIMAL,
    chain6: DataTypes.DECIMAL
  }, {
    sequelize,
    modelName: 'output',
  });
  return output;
};