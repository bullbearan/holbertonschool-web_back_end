const createInt8TypedArray = (length, postion, value) => {
  if (postion > length) throw Error('Position outside range');

  const int8View = new Int8Array(length);
  int8View[postion] = value;
  const { buffer } = int8View;
  return new DataView(buffer, 0, length);
};
export default createInt8TypedArray;
