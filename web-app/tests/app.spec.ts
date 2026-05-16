import { test, expect } from '@playwright/test';

test('basic navigation and practice', async ({ page }) => {
  await page.goto('http://localhost:4173');

  // Wait for the app to load
  await page.waitForSelector('h1');

  // Check title
  await expect(page.locator('h1')).toContainText('Fast Math Trainer');

  // Select a new rule: Square Root
  await page.click('h3:has-text("Square Root (Perfect)")');

  // Check if practice area is visible
  await expect(page.locator('text=How it works')).toBeVisible();

  // Screenshot
  await page.screenshot({ path: 'screenshot-sqrt.png' });

  // Back to methods
  await page.click('text=Back to methods');
  await expect(page.locator('text=Master Rapid Calculation')).toBeVisible();

  // Select a new rule: Rapid Addition
  await page.click('h3:has-text("Rapid Addition")');
  await page.screenshot({ path: 'screenshot-addition.png' });
});
