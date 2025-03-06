package ter0minator.untiered;

import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.init.Items;
import net.minecraft.item.ItemStack;

public class UntieredTab extends CreativeTabs {
    public UntieredTab(String label) {
        super(label);
    }

	@Override
	public ItemStack getTabIconItem() {
		return new ItemStack(UntieredEventHandler.CRONUS);
	}
}