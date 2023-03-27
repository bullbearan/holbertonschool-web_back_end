const getStudentsByLocation = (ss, city) => ss.filter((s) => (s.location === city));
export default getStudentsByLocation;
