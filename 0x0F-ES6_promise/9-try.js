export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const dividend = mathFunction();
    queue.push(dividend);
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
