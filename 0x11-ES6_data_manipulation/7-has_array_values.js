const hasValuesFromArray = (set, array) => {
  for (let idx = 0; idx < array.length; idx += 1) if (!set.has(array[idx])) return false;
  return true;
};
export default hasValuesFromArray;
