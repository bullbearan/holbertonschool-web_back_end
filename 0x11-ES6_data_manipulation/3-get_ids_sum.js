const getStudentIdsSum = (ss) => ss.reduce((total, n) => total + n.id, 0);
export default getStudentIdsSum;
