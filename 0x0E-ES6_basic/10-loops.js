export default function appendToEachArrayValue(array, appendString) {
  const a = [];
  for (const word of array) {
    a.push(appendString + word);
  }
  return a;
}
