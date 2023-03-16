export default function createIteratorObject(report) {
  let a = [];
  for (const value of Object.values(report.allEmployees)) {
    a = [...a, ...value];
  }

  return a;
}
