import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const arr = [19, 20, 34];
  return arr.map((num) => new ClassRoom(num));
}
