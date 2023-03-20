import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const user = await signUpUser(firstName, lastName)
    .then((response) => ({ status: 'success', response }))
    .catch((error) => ({ status: 'reject', value: error }));

  const photo = await uploadPhoto(fileName)
    .catch((error) => ({
      status: 'reject',
      value: `${error.name}: ${error.message}`,
    }));

  return [user, photo];
}
